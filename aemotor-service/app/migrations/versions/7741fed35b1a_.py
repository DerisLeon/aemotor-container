"""empty message

Revision ID: 7741fed35b1a
Revises: 
Create Date: 2023-04-13 00:11:50.866779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7741fed35b1a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_aluno',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('instituicaoDeEnsino', sa.String(), nullable=False),
    sa.Column('curso', sa.String(), nullable=False),
    sa.Column('matricula', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('matricula')
    )
    op.create_table('tb_pessoa',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=True),
    sa.Column('senha', sa.String(length=300), nullable=False),
    sa.Column('telefone', sa.String(length=11), nullable=True),
    sa.Column('nascimento', sa.Date(), nullable=True),
    sa.Column('tipo_pessoa', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('nome'),
    sa.UniqueConstraint('senha')
    )
    op.create_table('tb_endereco',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cep', sa.String(length=8), nullable=False),
    sa.Column('numero', sa.String(length=9), nullable=False),
    sa.Column('complemento', sa.String(), nullable=False),
    sa.Column('referencia', sa.String(), nullable=False),
    sa.Column('logradouro', sa.String(), nullable=False),
    sa.Column('pessoa_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pessoa_id'], ['tb_pessoa.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_funcionario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('prefeitura', sa.String(), nullable=False),
    sa.Column('cargo', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['tb_pessoa.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_funcionario')
    op.drop_table('tb_endereco')
    op.drop_table('tb_pessoa')
    op.drop_table('tb_aluno')
    # ### end Alembic commands ###
